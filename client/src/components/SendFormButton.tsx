import React from "react";
import { Button } from "@mui/material";
import {
  Lock as LockIcon,
  LockOpen as LockOpenIcon,
} from "@mui/icons-material";
import Severity from "@defined/severity";
import APIClient from "@utils/api-client";
import APIError from "@utils/api-error";

interface SendFormButtonProps {
  path: string;
  isEncrypt: boolean;
  query: Record<string, string>;
  fileInput: File | undefined;
  setLoading: React.Dispatch<React.SetStateAction<boolean>>;
  setFileOutput: React.Dispatch<React.SetStateAction<File | undefined>>;
  setOpenAlert: React.Dispatch<React.SetStateAction<boolean>>;
  setSeverity: React.Dispatch<React.SetStateAction<Severity>>;
  setMessage: React.Dispatch<React.SetStateAction<string>>;
}

type SendFormButtonComponent = ({}: SendFormButtonProps) => JSX.Element;

const SendFormButton: SendFormButtonComponent = (
  props: SendFormButtonProps
) => {
  const handleSend = async () => {
    if (!props.fileInput) {
      return;
    }

    props.setLoading(true);
    const response = await APIClient.Post(
      props.path,
      props.query,
      props.fileInput
    );
    props.setLoading(false);

    if (response instanceof File) {
      const message = `${response.name} berhasil diproses!`;

      props.setFileOutput(response);
      props.setSeverity("success");
      props.setMessage(message);
      props.setOpenAlert(true);
    } else {
      const { detail: listOfDetails } = response;
      const detail = listOfDetails[0];
      const { loc, msg, type } = detail;
      const message = `${type}: ${msg} (in ${loc.join(", ")})`;

      props.setFileOutput(undefined);
      props.setSeverity("error");
      props.setMessage(message);
      props.setOpenAlert(true);
    }
  };

  return (
    <Button
      variant="contained"
      component="label"
      startIcon={props.isEncrypt ? <LockIcon /> : <LockOpenIcon />}
      onClick={handleSend}
    >
      {props.isEncrypt ? "Encrypt" : "Decrypt"}
    </Button>
  );
};

export default SendFormButton;
