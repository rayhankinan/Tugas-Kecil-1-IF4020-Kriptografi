import fs from "fs";

class TempFile {
  private readonly fileName: string;

  constructor(fileName: string) {
    this.fileName = fileName;
  }

  public getWriteableStream() {
    const writeStream = fs.createWriteStream(this.fileName);
    return writeStream;
  }

  public readFile() {
    const buffer = fs.readFileSync(this.fileName);
    return new File([buffer], this.fileName);
  }

  public deletePath() {
    fs.unlinkSync(this.fileName);
  }
}

export default TempFile;
