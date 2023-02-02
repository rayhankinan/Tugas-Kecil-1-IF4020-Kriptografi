import React from "react";

interface DownloadFileProps {
  fileOutput: File | undefined;
}

type DownloadFileInfo = [
  ref: React.MutableRefObject<HTMLAnchorElement | null>,
  name: string | undefined,
  url: string | undefined,
  download: () => void
];

type DownloadFileHook = ({}: DownloadFileProps) => DownloadFileInfo;

const useDownloadFile: DownloadFileHook = ({
  fileOutput,
}: DownloadFileProps) => {
  const ref = React.useRef<HTMLAnchorElement | null>(null);
  const [name, setFileName] = React.useState<string>();
  const [url, setFileUrl] = React.useState<string>();

  const download = () => {
    if (!fileOutput) return;

    const newUrl = URL.createObjectURL(fileOutput);
    setFileUrl(newUrl);
    setFileName(fileOutput.name);

    console.log(newUrl);

    ref.current?.click();
    URL.revokeObjectURL(newUrl);
  };

  return [ref, name, url, download];
};

export default useDownloadFile;
