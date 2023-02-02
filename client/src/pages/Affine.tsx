import React from "react";
import { Container, Stack } from "@mui/material";
import useDeepCompareEffect from "@hooks/deep-compare-effect";
import Operation from "@defined-types/operation";
import PageLayout from "@layout/PageLayout";
import UploadDisplayText from "@components/UploadDisplayText";
import UploadFileButton from "@components/UploadFileButton";
import InputQuery from "@components/InputQuery";
import InputOperation from "@components/InputOperation";

const Affine: React.FC = () => {
  const [displayText, setDisplayText] = React.useState<string>();
  const [fileInput, setFileInput] = React.useState<File>();
  const [query, setQuery] = React.useState<Record<string, string>>({ key: "" });
  const [operation, setOperation] = React.useState<Operation>("encrypt-file");

  useDeepCompareEffect(() => {
    if (!fileInput) return;

    const reader = new FileReader();
    reader.onload = (evt) => {
      if (!evt.target) return;
      setDisplayText(evt.target.result as string);
    };

    reader.readAsText(fileInput);
  }, [fileInput]);

  return (
    <PageLayout>
      <Stack direction="row" spacing={2}>
        <Container maxWidth="lg">
          <Stack direction="column" spacing={2}>
            <UploadDisplayText
              displayText={displayText}
              setDisplayText={setDisplayText}
            />
            <UploadFileButton
              fileInput={fileInput}
              setFileInput={setFileInput}
            />
            <InputQuery parameter="key" query={query} setQuery={setQuery} />
            <InputOperation operation={operation} setOperation={setOperation} />
          </Stack>
        </Container>
        <Container maxWidth="lg">{/* Output */}</Container>
      </Stack>
    </PageLayout>
  );
};

export default Affine;
