import Axios, { AxiosError } from "axios";
import APIError from "@utils/api-error";

class APIClient {
  public static readonly API_HOST = import.meta.env.VITE_API_HOST || "/api";
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
  ): Promise<string | APIError> {
    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await Axios.post<string>(
        `${APIClient.API_HOST}${path}`,
        formData,
        {
          params: {
            ...query,
            access_token: APIClient.API_KEY,
          },
          responseType: "stream",
        }
      );

      return response.data;
    } catch (err: any) {
      return APIClient.HandleError(err);
    }
  }
}

export default APIClient;
