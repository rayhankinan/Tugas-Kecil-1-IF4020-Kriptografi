import Axios, { AxiosError } from "axios";
import APIError from "@utils/api-error";

class APIClient {
  public static readonly API_HOST = import.meta.env.VITE_API_HOST || "/api";
  public static readonly API_KEY = import.meta.env.VITE_API_KEY || "api-key";

  private static HandleError(err: any): APIError {
    const emptyError: APIError = {
      detail: [],
    };

    if (err instanceof AxiosError) {
      const { response } = err as AxiosError;

      if (response) {
        return JSON.parse(response.data as string) as APIError;
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
    } catch (err) {
      return APIClient.HandleError(err);
    }
  }
}

export default APIClient;
