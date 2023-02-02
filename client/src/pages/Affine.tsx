import React from "react";
import PageLayout from "@layout/PageLayout";
import useDeepCompareEffect from "@hooks/deep-compare-effect";
import AlertProps from "@interface/alert-props";
import UploadDisplayText from "@components/UploadDisplayText";
import UploadFileButton from "@components/UploadFileButton";

const Affine: React.FC = () => {
  const [displayText, setDisplayText] = React.useState<string>();
  const [fileInput, setFileInput] = React.useState<File>();
  const [alertProps, setAlertProps] = React.useState<AlertProps>();

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
      <UploadDisplayText
        displayText={displayText}
        setDisplayText={setDisplayText}
      />
      <UploadFileButton fileInput={fileInput} setFileInput={setFileInput} />
    </PageLayout>
  );
};

export default Affine;
