import React from "react";
import { Button, CircularProgress } from "@mui/material";
import {
  Lock as LockIcon,
  LockOpen as LockOpenIcon,
} from "@mui/icons-material";
import APIClient from "@utils/api-client";
import AlertProps from "@interface/alert-props";
import FileWritableStream from "@utils/file-writable-stream";
import StringReadableStream from "@utils/string-readable-stream";

interface SendFormButtonProps {
  path: string;
  isEncrypt: boolean;
  query: Record<string, string>;
  displayText: string | undefined;
  fileInput: File | undefined;
  setLoading: React.Dispatch<React.SetStateAction<boolean>>;
  setFileOutput: React.Dispatch<React.SetStateAction<File | undefined>>;
  setAlert: React.Dispatch<React.SetStateAction<AlertProps | undefined>>;
}

const SendFormButton: React.FC<SendFormButtonProps> = ({
  path,
  isEncrypt,
  query,
  displayText,
  fileInput,
  setLoading,
  setFileOutput,
  setAlert,
}: SendFormButtonProps) => {
  const handleSend = async () => {
    if (!displayText) return;

    setLoading(true);
    const stringReadableStream = new StringReadableStream(displayText);
    const fileWriteableStream = new FileWritableStream(
      fileInput ? fileInput.name : ".txt"
    );
    stringReadableStream.pipe(fileWriteableStream);
    const file = fileWriteableStream.getFile();

    const response = await APIClient.Post(path, query, file);

    if (response instanceof File) {
      const message = `${response.name} berhasil diproses!`;

      setFileOutput(response);
      setAlert({
        openAlert: true,
        message,
        severity: "success",
      });
    } else {
      const { detail: listOfDetails } = response;
      const detail = listOfDetails[0];
      const { loc, msg, type } = detail;
      const message = `${type}: ${msg} (in ${loc.join(", ")})`;

      setAlert({
        openAlert: true,
        message,
        severity: "error",
      });
    }

    setLoading(false);
  };

  return (
    <Button
      variant="contained"
      component="label"
      startIcon={isEncrypt ? <LockIcon /> : <LockOpenIcon />}
      onClick={handleSend}
    >
      {isEncrypt ? "Encrypt" : "Decrypt"}
    </Button>
  );
};

export default SendFormButton;
