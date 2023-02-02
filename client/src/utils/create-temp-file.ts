import { temporaryFile } from "tempy";
import fs from "fs";

class TempFile {
  private readonly fileName: string;
  private readonly path: string;

  constructor(fileName: string) {
    this.fileName = fileName;
    this.path = temporaryFile({ name: fileName });
  }

  public getWriteableStream() {
    const writeStream = fs.createWriteStream(this.path);
    return writeStream;
  }

  public readFile() {
    const buffer = fs.readFileSync(this.path);
    return new File([buffer], this.fileName);
  }

  public deletePath() {
    fs.unlinkSync(this.path);
  }
}

export default TempFile;
