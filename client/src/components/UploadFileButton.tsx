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

const UploadFileButton: React.FC<UploadFileButtonProps> = (
  props: UploadFileButtonProps
) => {
  const handleUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { files } = event.target;
    const selectedFiles = files as FileList;
    const currentFile = selectedFiles?.[0];

    props.setFileInput(currentFile);
  };

  return (
    <Button
      variant="contained"
      component="label"
      startIcon={props.fileInput ? <AttachmentIcon /> : <UploadIcon />}
    >
      {props.fileInput ? props.fileInput.name : "Upload"}
      <input hidden type="file" onChange={handleUpload} />
    </Button>
  );
};

export default UploadFileButton;
