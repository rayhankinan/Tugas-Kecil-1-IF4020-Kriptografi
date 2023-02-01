import React from "react";
import { Alert, Snackbar } from "@mui/material";
import Severity from "@defined/severity";

interface ResultDisplayAlertProps {
  openAlert: boolean;
  setOpenAlert: React.Dispatch<React.SetStateAction<boolean>>;
  severity: Severity;
  message: string;
}

const ResultDisplayAlert: React.FC<ResultDisplayAlertProps> = (
  props: ResultDisplayAlertProps
) => {
  const handleClose = () => {
    props.setOpenAlert(false);
  };

  return (
    <Snackbar
      open={props.openAlert}
      autoHideDuration={1000}
      onClose={handleClose}
    >
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
