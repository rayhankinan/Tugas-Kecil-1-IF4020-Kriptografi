import { Button } from "@mui/material";
import { Download as DownloadIcon } from "@mui/icons-material";
import useDownloadFile from "@hooks/download-file";
import React from "react";

interface DownloadFileButtonProps {
  fileOutput: File | undefined;
}

const DownloadFileButton: React.FC<DownloadFileButtonProps> = ({
  fileOutput,
}: DownloadFileButtonProps) => {
  const [ref, name, url, download] = useDownloadFile({
    fileOutput,
  });

  return (
    <React.Fragment>
      <a href={url} download={name} ref={ref} hidden />
      <Button
        variant="contained"
        component="label"
        startIcon={<DownloadIcon />}
        onClick={download}
      >
        Download
      </Button>
    </React.Fragment>
  );
};

export default DownloadFileButton;
