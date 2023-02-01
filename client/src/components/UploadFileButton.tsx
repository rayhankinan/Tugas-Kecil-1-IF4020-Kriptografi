import React from "react";
import { Button } from "@mui/material";
import {
  Attachment as AttachmentIcon,
  Upload as UploadIcon,
} from "@mui/icons-material";

interface UploadFileButtonProps {
  file: File | null;
  setFile: React.Dispatch<React.SetStateAction<File | null>>;
}

type UploadFileButtonComponent = ({}: UploadFileButtonProps) => JSX.Element;

const UploadFileButton: UploadFileButtonComponent = (
  props: UploadFileButtonProps
) => {
  const handleUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { files } = event.target;
    const selectedFiles = files as FileList;
    const currentFile = selectedFiles?.[0];

    props.setFile(currentFile);
  };

  return (
    <Button
      variant="contained"
      component="label"
      startIcon={props.file ? <AttachmentIcon /> : <UploadIcon />}
    >
      {props.file ? props.file.name : "Upload"}
      <input hidden type="file" onChange={handleUpload} />
    </Button>
  );
};

export default UploadFileButton;
