import React from "react";

interface DownloadFileProps {
  file: File | null;
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
    if (!props.file) {
      return;
    }

    const url = URL.createObjectURL(props.file);
    setFileUrl(url);
    setFileName(props.file.name);
    ref.current?.click();
    URL.revokeObjectURL(url);
  };

  return { ref, name, url, download };
};

export default useDownloadFile;
