import stream from "stream";

class StringReadableStream extends stream.Readable {
  constructor(content: string) {
    super();
    this.push(content);
    this.push(null);
  }
}

export default StringReadableStream;
