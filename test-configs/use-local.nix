let
  mxklabs = import <mxklabs>;
in
  {
    mxklabs-example-cpp-app = mxklabs.mxklabs-example-cpp-app.overrideAttrs (oldAttrs: {
        src = ../../mxklabs-example-cpp-app;
      });
    mxklabs-example-cpp-lib1 = mxklabs.mxklabs-example-cpp-lib1.overrideAttrs (oldAttrs: {
        src = ../../mxklabs-example-cpp-lib1;
      });
  }

