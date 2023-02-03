import React from "react";
import { Container, Stack } from "@mui/material";
import useDeepCompareEffect from "@hooks/deep-compare-effect";
import Operation from "@defined-types/operation";
import AlertProps from "@interface/alert-props";
import PageLayout from "@layout/PageLayout";
import UploadDisplayText from "@components/UploadDisplayText";
import UploadFileButton from "@components/UploadFileButton";
import ClearFileButton from "@components/ClearFileButton";
import InputQuery from "@components/InputQuery";
import InputOperation from "@components/InputOperation";
import SendFormButton from "@components/SendFormButton";
import ResultDisplayAlert from "@components/ResultDisplayAlert";
import ResultDisplayText from "@components/ResultDisplayText";
import SwitchDisplayView from "@components/SwitchDisplayView";
import DownloadFileButton from "@components/DownloadFileButton";

const Affine: React.FC = () => {
  // Input
  const [displayTextInput, setDisplayTextInput] = React.useState<string>();
  const [fileInput, setFileInput] = React.useState<File>();
  const [query, setQuery] = React.useState<Record<string, string>>({
    key: "",
    shift: "",
  });
  const [operation, setOperation] = React.useState<Operation>("encrypt-file");

  // Output
  const [displayTextOutput, setDisplayTextOutput] = React.useState<string>();
  const [fileOutput, setFileOutput] = React.useState<File>();
  const [isSeparated, setIsSeparated] = React.useState<boolean>(false);

  // Notification
  const [alertProps, setAlertProps] = React.useState<AlertProps>({
    openAlert: false,
    severity: "error",
    message: "",
  });

  useDeepCompareEffect(() => {
    if (!fileInput) return;

    const reader = new FileReader();
    reader.onload = (evt) => {
      if (!evt.target) return;
      setDisplayTextInput(evt.target.result as string);
    };

    reader.readAsBinaryString(fileInput);
  }, [fileInput]);

  useDeepCompareEffect(() => {
    if (!fileOutput) return;

    const reader = new FileReader();
    reader.onload = (evt) => {
      if (!evt.target) return;
      setDisplayTextOutput(evt.target.result as string);
    };

    reader.readAsBinaryString(fileOutput);
  }, [fileOutput]);

  return (
    <PageLayout>
      <Stack direction="row" spacing={2}>
        <Container maxWidth="lg">
          <Stack direction="column" spacing={2}>
            <UploadDisplayText
              placeholder="Affine Cipher"
              displayText={displayTextInput}
              setDisplayText={setDisplayTextInput}
            />
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
            <InputQuery
              parameter="shift"
              placeholder="Shift"
              query={query}
              setQuery={setQuery}
            />
            <InputOperation operation={operation} setOperation={setOperation} />
            <SendFormButton
              path="/affine"
              operation={operation}
              query={query}
              displayText={displayTextInput}
              fileInput={fileInput}
              setFileOutput={setFileOutput}
              setAlertProps={setAlertProps}
            />
          </Stack>
        </Container>
        <Container maxWidth="lg">
          <Stack direction="column" spacing={2}>
            <ResultDisplayText
              placeholder="Output"
              displayText={displayTextOutput}
              isSeparated={isSeparated}
            />
            <SwitchDisplayView
              isSeparated={isSeparated}
              setIsSeparated={setIsSeparated}
            />
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

export default Affine;
