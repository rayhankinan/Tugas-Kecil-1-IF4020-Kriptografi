import React from "react";
import { Button, CircularProgress } from "@mui/material";
import {
  Lock as LockIcon,
  LockOpen as LockOpenIcon,
} from "@mui/icons-material";
import { AxiosProgressEvent } from "axios";
import APIClient from "@utils/api-client";
import AlertProps from "@interface/alert-props";

interface SendFormButtonProps {
  path: string;
  isEncrypt: boolean;
  query: Record<string, string>;
  fileInput: File | undefined;
  setFileOutput: React.Dispatch<React.SetStateAction<File | undefined>>;
  setAlert: React.Dispatch<React.SetStateAction<AlertProps | undefined>>;
}

const SendFormButton: React.FC<SendFormButtonProps> = ({
  path,
  isEncrypt,
  query,
  fileInput,
  setFileOutput,
  setAlert,
}: SendFormButtonProps) => {
  const [progressUpload, setProgressUpload] = React.useState<number>(100);

  const handleSend = async () => {
    if (!fileInput) return;

    setProgressUpload(0);
    const response = await APIClient.Post(
      path,
      query,
      fileInput,
      (progressEvent: AxiosProgressEvent) => {
        if (!progressEvent.total) return;

        setProgressUpload(
          Math.round(100 * progressEvent.loaded) / progressEvent.total
        );
      }
    );

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
  };

  const getStartIcon = () => {
    if (progressUpload < 100) {
      return <CircularProgress value={progressUpload} />;
    } else if (isEncrypt) {
      return <LockIcon />;
    } else {
      return <LockOpenIcon />;
    }
  };

  const getMessage = () => {
    if (progressUpload < 100) {
      return "Uploading";
    } else if (isEncrypt) {
      return "Encrypt";
    } else {
      return "Decrypt";
    }
  };

  return (
    <Button
      variant="contained"
      component="label"
      startIcon={getStartIcon()}
      onClick={handleSend}
    >
      {getMessage()}
    </Button>
  );
};

export default SendFormButton;
