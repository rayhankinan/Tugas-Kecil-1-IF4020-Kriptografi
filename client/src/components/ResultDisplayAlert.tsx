import React from "react";
import { Alert, Snackbar } from "@mui/material";

type Severity = "error" | "success";

interface ResultDisplayAlertProps {
  open: boolean;
  setOpen: React.Dispatch<React.SetStateAction<boolean>>;
  severity: Severity;
  message: string;
}

type ResultDisplayAlertComponent = ({}: ResultDisplayAlertProps) => JSX.Element;

const ResultDisplayAlert: ResultDisplayAlertComponent = (
  props: ResultDisplayAlertProps
) => {
  const handleClose = () => {
    props.setOpen(false);
  };

  return (
    <Snackbar open={props.open} autoHideDuration={1000} onClose={handleClose}>
      <Alert
        onClose={handleClose}
        severity={props.severity}
        sx={{ width: "100%" }}
      >
        {props.message}
      </Alert>
    </Snackbar>
  );
};

export default ResultDisplayAlert;
