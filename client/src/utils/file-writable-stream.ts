import stream from "stream";

class FileWritableStream extends stream.Writable {
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

export default FileWritableStream;
