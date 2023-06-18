import cx_Freeze
executables =[
    cx_Freeze.Executable(script="main.py", icon="logo.ico")
]
cx_Freeze.setup(
    name = "Space Marker",
    options={
        "build_exe":{
            "packages":["pygame", "simpledialog"],
            "include_files":["image.jpeg",
                            "logo.png",
                            
                            "Space_Machine_Power.mp3"]
        }
    }, executables = executables
)

#py setup.py build
