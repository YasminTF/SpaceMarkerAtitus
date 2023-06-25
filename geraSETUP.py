import cx_Freeze
executables =[
    cx_Freeze.Executable(script="main.py", icon="logo.png")
]
cx_Freeze.setup(
    name = "Space Marker",
    options={
        "build_exe":{
            "packages":["pygame",],
            "include_files":["image.jpeg",
                            "logo.png",
                            "banco_dados",
                            "Space_Machine_Power.mp3"]
        }
    }, executables = executables
)

#py setup.py build
