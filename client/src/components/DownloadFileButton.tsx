import { Button } from "@mui/material";
import { Download as DownloadIcon } from "@mui/icons-material";
import React from "react";

interface DownloadFileButtonProps {
  fileOutput: File | undefined;
  disabled: boolean;
}

const DownloadFileButton: React.FC<DownloadFileButtonProps> = ({
  fileOutput,
  disabled,
}: DownloadFileButtonProps) => {
  const download = () => {
    if (!fileOutput) return;

    const url = URL.createObjectURL(fileOutput);

    const a = document.createElement("a");
    a.href = url;
    a.download = fileOutput.name;

    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);

    URL.revokeObjectURL(url);
  };

  return (
    <React.Fragment>
      <Button
        variant="contained"
        component="label"
        startIcon={<DownloadIcon />}
        onClick={download}
        disabled={disabled}
      >
        Download
      </Button>
    </React.Fragment>
  );
};

export default DownloadFileButton;
