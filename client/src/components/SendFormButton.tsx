import React from "react";
import { Button } from "@mui/material";
import {
  Lock as LockIcon,
  LockOpen as LockOpenIcon,
} from "@mui/icons-material";
import APIClient from "@utils/api-client";
import AlertProps from "@interface/alert-props";
import Operation from "@defined-types/operation";

interface SendFormButtonProps {
  path: string;
  operation: Operation;
  query: Record<string, string>;
  displayText: string | undefined;
  fileInput: File | undefined;
  setFileOutput: React.Dispatch<React.SetStateAction<File | undefined>>;
  setAlertProps: React.Dispatch<React.SetStateAction<AlertProps>>;
}

const SendFormButton: React.FC<SendFormButtonProps> = ({
  path,
  operation,
  query,
  displayText,
  fileInput,
  setFileOutput,
  setAlertProps,
}: SendFormButtonProps) => {
  const handleSend = async () => {
    if (!displayText) return;

    const fileRequest = new File(
      [displayText],
      fileInput ? fileInput.name : ".txt"
    );
    const response = await APIClient.Post(
      `${path}/${operation}`,
      query,
      fileRequest
    );

    if (typeof response === "string") {
      const fileResponse = new File([response as BlobPart], fileRequest.name);
      setFileOutput(fileResponse);

      const message = `${fileRequest.name} berhasil diproses!`;
      setAlertProps({
        openAlert: true,
        message,
        severity: "success",
      });
    } else {
      setFileOutput(undefined);

      const { detail: listOfDetails } = response;
      const detail = listOfDetails[0];
      const { loc, msg, type } = detail;
      const message = `${type}: ${msg} (in ${loc.join(", ")})`;

      setAlertProps({
        openAlert: true,
        message,
        severity: "error",
      });
    }
  };

  return (
    <Button
      variant="contained"
      component="label"
      startIcon={operation === "encrypt-file" ? <LockIcon /> : <LockOpenIcon />}
      onClick={handleSend}
    >
      {operation === "encrypt-file" ? "Encrypt" : "Decrypt"}
    </Button>
  );
};

export default SendFormButton;
