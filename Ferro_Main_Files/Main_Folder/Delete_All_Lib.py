import subprocess
import pkg_resources
from Style import Animations
from Other.Code import Vari_And_Func as Var

installed_packages = [pkg.key for pkg in pkg_resources.working_set]

for package in installed_packages:
    subprocess.run(["pip", "uninstall", "-y", package])

print(Var.Space_Big)
print("All Files Are Deleted.....")
print(Var.Space_Big)
Animations.loading_animation(total_time=3 , width=120)
print(Var.Space_Big)
print("Closed Program :)")