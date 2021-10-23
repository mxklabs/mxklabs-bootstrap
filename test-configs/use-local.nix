let
  mxklabs-pkgs = import ../../mxklabs-pkgs/default.nix /*<mxklabs>*/ { overlays = [ overlay ]; };
  overlay = final: prev: {
    mxklabs-example-cpp-app = prev.mxklabs-example-cpp-app.overrideAttrs (oldAttrs: {
        src = ../../mxklabs-example-cpp-app;
      });
    mxklabs-example-cpp-lib1 = prev.mxklabs-example-cpp-lib1.overrideAttrs (oldAttrs: {
        src = ../../mxklabs-example-cpp-lib1;
      });
  };
in
  mxklabs-pkgs

