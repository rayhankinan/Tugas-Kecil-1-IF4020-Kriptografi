import Axios, { AxiosError } from "axios";
import stream from "stream";
import fs from "fs";

interface APIErrorDetail {
  loc: string[];
  msg: string;
  type: string;
}

interface APIError {
  detail: APIErrorDetail[];
}

class FileStream extends stream.Writable {
  private readonly fileBits: BlobPart[];
  private readonly fileName: string;

  constructor(fileName: string) {
    super();
    this.fileBits = [];
    this.fileName = fileName;
  }

  _write(
    chunk: any,
    encoding: BufferEncoding,
    callback: (error?: Error | null | undefined) => void
  ): void {
    this.fileBits.push(chunk as BlobPart);
    callback();
  }

  getFile() {
    return new File(this.fileBits, this.fileName);
  }
}

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
