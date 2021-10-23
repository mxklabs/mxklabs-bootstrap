let
  mxklabs-pkgs = import /*../../mxklabs-pkgs/default.nix*/ <mxklabs> { overlays = [ overlay ]; };
  overlay = final: prev: {
    mxklabs-example-cpp-app = prev.mxklabs-example-cpp-app.overrideAttrs (oldAttrs: {
        src = builtins.fetchGit {
          url    = "git@github.com:mxklabs/mxklabs-example-cpp-app.git";
          ref    = "master";
          rev    = "76e552674864efa2737c38c0b283a611940a3771";
          #rev    = "55ae05fcc671ad4414317a36fad31c710aa093d7";
        };
      });
    mxklabs-example-cpp-lib1 = prev.mxklabs-example-cpp-lib1.overrideAttrs (oldAttrs: {
        src = builtins.fetchGit {
          url    = "git@github.com:mxklabs/mxklabs-example-cpp-lib1.git";
          ref    = "master";
          #rev    = "407a282bb142a96c88ba60ff8da641e128c82a2a";
          rev    = "ff39ee33755499da8af9296ebc50993cef2d1ce1";
          #rev    = "033152d0bd47a97975caaebaf765dd35e11b6b8a";
          #rev    = "1e4df3ae520734cad9ce6f3d39a06c0c1ba1a03c";
          #rev    = "efdb78f4529d4892591aab63972fec8bd4fdaf99";
        };
      });
  };
in
  mxklabs-pkgs
