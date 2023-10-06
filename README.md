# Conan-stubs
Type stubs for specific conan versions for authoring Conanfiles.
Versions of this package will correspond to the corresponding conan minor version.

* Generated with mypy via `stubgen -p conans --include-private` to fill up package, so everything resolves
* model.conan_file is handcrafted and functions are documented with basic descriptions
* Selectable string values are annotated (e.g. all generators) and scm attribute is fully typehinted as typeddcit

## Limitations

* tool_requires, build_requires, requires are annotated with only their function signature
* settings are annotated by their setter information for the class variable
* Every annotation is in the file, but commented out

### Details

Methods which also can be used as class variables can not be annotated directly:
`
...
    tool_requires = "cmake/3.25.3"
    def build_requirements(self):
        self.tool_requires("cmake/3.25.3")
`

The annotation would look like this with a property + method, but can not interpreted:
`
    @property
    @overload
    def tool_requires(self) -> None: ...
    @overload
    def tool_requires(self, requirement: str, force_host_context: bool=False) -> None: ...
    @tool_requires.setter
    def tool_requires(self, value: Optional[Iterable[str]]): ...
`


## Supported conan versions:
  * 1.59.0

## Supported Python versions:
  * >=3.8


