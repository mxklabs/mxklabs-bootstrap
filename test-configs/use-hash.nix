let
  mxklabs = import <mxklabs>;
in
  {
    mxklabs-example-cpp-app = mxklabs.mxklabs-example-cpp-app.overrideAttrs (oldAttrs: {
        src = ../../mxklabs-example-cpp-app;
      });
    mxklabs-example-cpp-lib1 = mxklabs.mxklabs-example-cpp-lib1.overrideAttrs (oldAttrs: {
        src = builtins.fetchGit {
          url    = "git@github.com:mxklabs/mxklabs-example-cpp-lib1.git";
          rev    = "efdb78f4529d4892591aab63972fec8bd4fdaf99";
        };
      });
  }

