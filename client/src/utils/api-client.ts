import Axios, { AxiosError } from "axios";
import fs from "fs";
import APIError from "@utils/api-error";
import FileStream from "@utils/file-stream";

class APIClient {
  public static readonly API_HOST = process.env.API_HOST || "localhost";
  public static readonly API_KEY = process.env.API_KEY || "api-key";

  private static HandleError(rawError: any): APIError {
    const emptyError: APIError = {
      detail: [],
    };

    if (rawError instanceof AxiosError) {
      const { response } = rawError as AxiosError;
      if (response) {
        return response.data as APIError;
      }
      return emptyError;
    }
    return emptyError;
  }

  public static async Post(
    path: string,
    query: Record<string, string>,
    body: Record<string, File>,
    fileName: string
  ): Promise<File | APIError> {
    try {
      const response = await Axios.post<fs.ReadStream>(
        `${APIClient.API_HOST}${path}`,
        body,
        {
          params: {
            access_token: APIClient.API_KEY,
            ...query,
          },
          responseType: "stream",
        }
      );

      const fileStream = new FileStream(fileName);
      response.data.pipe(fileStream);

      return fileStream.getFile();
    } catch (err: any) {
      return APIClient.HandleError(err);
    }
  }
}

export default APIClient;
