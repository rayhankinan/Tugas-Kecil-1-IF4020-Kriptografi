import React from "react";
import { Button } from "@mui/material";
import {
  Lock as LockIcon,
  LockOpen as LockOpenIcon,
} from "@mui/icons-material";
import APIClient from "@utils/api-client";
import AlertProps from "@interface/alert-props";
import Operation from "@defined-types/operation";

interface SendFileButtonProps {
  path: string;
  operation: Operation;
  query: Record<string, string>;
  fileInput: File | undefined;
  setFileOutput: React.Dispatch<React.SetStateAction<File | undefined>>;
  setAlertProps: React.Dispatch<React.SetStateAction<AlertProps>>;
}

const SendFileButton: React.FC<SendFileButtonProps> = ({
  path,
  operation,
  query,
  fileInput,
  setFileOutput,
  setAlertProps,
}: SendFileButtonProps) => {
  const handleSend = async () => {
    if (!fileInput) return;

    const response = await APIClient.Post(
      `${path}/${operation}`,
      query,
      fileInput
    );

    if (response instanceof ArrayBuffer) {
      const fileResponse = new File([response], fileInput.name, {
        type: fileInput.type,
      });

      setFileOutput(fileResponse);

      const message = `${fileInput.name} berhasil diproses!`;
      setAlertProps({
        openAlert: true,
        message,
        severity: "success",
      });
    } else {
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

export default SendFileButton;
