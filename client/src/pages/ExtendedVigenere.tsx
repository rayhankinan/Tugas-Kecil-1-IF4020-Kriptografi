import React from "react";
import { Container, Stack } from "@mui/material";
import Operation from "@defined-types/operation";
import AlertProps from "@interface/alert-props";
import PageLayout from "@layout/PageLayout";
import UploadFileButton from "@components/UploadFileButton";
import ClearFileButton from "@components/ClearFileButton";
import InputQuery from "@components/InputQuery";
import InputOperation from "@components/InputOperation";
import SendFileButton from "@components/SendFileButton";
import ResultDisplayAlert from "@components/ResultDisplayAlert";
import DownloadFileButton from "@components/DownloadFileButton";

const ExtendedVigenere: React.FC = () => {
  // Input
  const [fileInput, setFileInput] = React.useState<File>();
  const [query, setQuery] = React.useState<Record<string, string>>({
    key: "",
    shift: "",
  });
  const [operation, setOperation] = React.useState<Operation>("encrypt-file");

  // Output
  const [fileOutput, setFileOutput] = React.useState<File>();

  // Notification
  const [alertProps, setAlertProps] = React.useState<AlertProps>({
    openAlert: false,
    severity: "error",
    message: "",
  });

  return (
    <PageLayout>
      <Stack direction="row" spacing={10}>
        <Container maxWidth="xl">
          <Stack direction="column" spacing={2}>
            <Stack direction={"row"} spacing={2}>
              <UploadFileButton
                fileInput={fileInput}
                setFileInput={setFileInput}
              />
              <ClearFileButton
                fileInput={fileInput}
                setFileInput={setFileInput}
              />
            </Stack>
            <InputQuery
              parameter="key"
              placeholder="Key"
              query={query}
              setQuery={setQuery}
            />
            <InputOperation operation={operation} setOperation={setOperation} />
            <SendFileButton
              path="/extended-vigenere"
              operation={operation}
              query={query}
              fileInput={fileInput}
              setFileOutput={setFileOutput}
              setAlertProps={setAlertProps}
            />
          </Stack>
        </Container>
        <Container maxWidth="xl">
          <Stack direction="column" spacing={2}>
            <DownloadFileButton fileOutput={fileOutput} />
          </Stack>
        </Container>
      </Stack>
      <ResultDisplayAlert
        alertProps={alertProps}
        setAlertProps={setAlertProps}
      />
    </PageLayout>
  );
};

export default ExtendedVigenere;
