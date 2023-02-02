import Axios, { AxiosError } from "axios";
import fs from "fs";
import APIError from "@utils/api-error";
import TempFile from "@utils/create-temp-file";

class APIClient {
  public static readonly API_HOST =
    import.meta.env.VITE_API_HOST || "localhost";
  public static readonly API_KEY = import.meta.env.VITE_API_KEY || "api-key";

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
    file: File
  ): Promise<TempFile | APIError> {
    try {
      const response = await Axios.post<fs.ReadStream>(
        `${APIClient.API_HOST}${path}`,
        { file },
        {
          params: {
            ...query,
            access_token: APIClient.API_KEY,
          },
          responseType: "stream",
        }
      );

      const tempFile = new TempFile(file.name);
      const fileWritableStream = tempFile.getWriteableStream();
      response.data.pipe(fileWritableStream);

      return tempFile;
    } catch (err: any) {
      return APIClient.HandleError(err);
    }
  }
}

export default APIClient;
