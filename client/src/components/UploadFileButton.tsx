import React from "react";
import { Button } from "@mui/material";
import {
  Attachment as AttachmentIcon,
  Upload as UploadIcon,
} from "@mui/icons-material";

interface UploadFileButtonProps {
  fileInput: File | undefined;
  setFileInput: React.Dispatch<React.SetStateAction<File | undefined>>;
}

const UploadFileButton: React.FC<UploadFileButtonProps> = ({
  fileInput,
  setFileInput,
}: UploadFileButtonProps) => {
  const handleUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { files } = event.target;
    const selectedFiles = files as FileList;
    const currentFile = selectedFiles?.[0];

    setFileInput(currentFile);
    event.target.value = "";
  };

  return (
    <Button
      variant="contained"
      component="label"
      startIcon={fileInput ? <AttachmentIcon /> : <UploadIcon />}
    >
      {fileInput ? fileInput.name : "Upload"}
      <input hidden type="file" onChange={handleUpload} />
    </Button>
  );
};

export default UploadFileButton;
