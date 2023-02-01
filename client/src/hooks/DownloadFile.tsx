import React from "react";

interface DownloadFileProps {
  fileOutput: File | undefined;
}

interface DownloadFileInfo {
  ref: React.MutableRefObject<HTMLAnchorElement | null>;
  name: string | undefined;
  url: string | undefined;
  download: () => Promise<void>;
}

type DownloadFileHook = ({}: DownloadFileProps) => DownloadFileInfo;

const useDownloadFile: DownloadFileHook = (props: DownloadFileProps) => {
  const ref = React.useRef<HTMLAnchorElement | null>(null);
  const [name, setFileName] = React.useState<string>();
  const [url, setFileUrl] = React.useState<string>();

  const download = async () => {
    if (!props.fileOutput) return;

    const url = URL.createObjectURL(props.fileOutput);
    setFileUrl(url);
    setFileName(props.fileOutput.name);
    ref.current?.click();
    URL.revokeObjectURL(url);
  };

  return { ref, name, url, download };
};

export default useDownloadFile;
