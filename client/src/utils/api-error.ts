interface APIErrorDetail {
  loc: string[];
  msg: string;
  type: string;
}

interface APIError {
  detail: APIErrorDetail[];
}

export default APIError;
