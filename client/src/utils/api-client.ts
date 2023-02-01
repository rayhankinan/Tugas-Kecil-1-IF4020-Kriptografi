import Axios, { AxiosError } from "axios";

interface APIResponse {
  file: Blob[];
}

interface APIErrorDetail {
  loc: string[];
  msg: string;
  type: string;
}

interface APIError {
  detail: APIErrorDetail[];
}

class APIClient {
  public static readonly API_HOST = process.env.API_HOST || "localhost";
  public static readonly API_KEY = process.env.API_KEY || "api-key";

  private static HandleError(rawError: any): APIError {
    const error: APIError = {
      detail: [],
    };

    if (rawError instanceof AxiosError) {
      const { response } = rawError as AxiosError;
      if (response) {
        error.detail = (response.data as APIError).detail;
      }
    }

    return error;
  }

  public static async Post(
    path: string,
    query: Record<string, string>,
    body: Record<string, File>
  ): Promise<APIResponse | APIError> {
    try {
      const response = await Axios.post<APIResponse>(
        `${APIClient.API_HOST}${path}`,
        body,
        {
          params: {
            access_token: APIClient.API_KEY,
            ...query,
          },
        }
      );

      return response.data;
    } catch (err: any) {
      return APIClient.HandleError(err);
    }
  }
}

export default APIClient;
