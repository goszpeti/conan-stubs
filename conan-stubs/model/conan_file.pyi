from _typeshed import Incomplete
from collections.abc import Generator
from conans.client import tools as tools
from conans.client.output import ScopedOutput as ScopedOutput
from conans.client.subsystems import command_env_wrapper as command_env_wrapper
from conans.client.tools.env import environment_append as environment_append, no_op as no_op, pythonpath as pythonpath
from conans.client.tools.oss import OSInfo as OSInfo
from conans.errors import ConanException as ConanException, ConanInvalidConfiguration as ConanInvalidConfiguration
from conans.model.build_info import DepsCppInfo as DepsCppInfo
from conans.model.conf import Conf as Conf
from conans.model.dependencies import ConanFileDependencies as ConanFileDependencies
from conans.model.env_info import DepsEnvInfo as DepsEnvInfo
from conans.model.layout import Folders as Folders, Infos as Infos, Layouts as Layouts
from conans.model.new_build_info import from_old_cppinfo as from_old_cppinfo
from conans.model.options import Options as Options, OptionsValues as OptionsValues, PackageOptions as PackageOptions
from conans.model.requires import Requirements as Requirements
from conans.model.user_info import DepsUserInfo as DepsUserInfo
from conans.paths import RUN_LOG_NAME as RUN_LOG_NAME
from conans.util.conan_v2_mode import conan_v2_error as conan_v2_error
from pathlib import Path

def create_options(conanfile): ...
def create_requirements(conanfile): ...
def create_settings(conanfile, settings): ...
def _env_and_python(conanfile) -> Generator[None, None, None]: ...
def get_env_context_manager(conanfile, without_python: bool = ...): ...

class ConanFile:
    name: Incomplete
    version: Incomplete
    url: Incomplete
    license: Incomplete
    author: Incomplete
    description: Incomplete
    topics: Incomplete
    homepage: Incomplete
    build_policy: Incomplete
    upload_policy: Incomplete
    short_paths: bool
    apply_env: bool
    exports: Incomplete
    exports_sources: Incomplete
    generators: Incomplete
    revision_mode: str
    should_configure: bool
    should_build: bool
    should_install: bool
    should_test: bool
    in_local_cache: bool
    develop: bool
    default_channel: Incomplete
    default_user: Incomplete
    settings: Incomplete
    options: Incomplete
    default_options: Incomplete
    provides: Incomplete
    deprecated: Incomplete
    folders: Incomplete
    patterns: Incomplete
    win_bash: Incomplete
    win_bash_run: Incomplete
    tested_reference_str: Incomplete
    output: Incomplete
    display_name: Incomplete
    _conan_runner: Incomplete
    _conan_user: Incomplete
    _conan_channel: Incomplete
    compatible_packages: Incomplete
    _conan_using_build_profile: bool
    _conan_requester: Incomplete
    buildenv_info: Incomplete
    runenv_info: Incomplete
    conf_info: Incomplete
    _conan_buildenv: Incomplete
    _conan_runenv: Incomplete
    _conan_node: Incomplete
    _conan_new_cpp_info: Incomplete
    _conan_dependencies: Incomplete
    env_scripts: Incomplete
    cpp: Incomplete
    layouts: Incomplete
    def __init__(self, output, runner, display_name: str = ..., user: Incomplete | None = ..., channel: Incomplete | None = ...) -> None: ...
    @property
    def context(self): ...
    @property
    def dependencies(self): ...
    @property
    def ref(self): ...
    @property
    def pref(self): ...
    @property
    def buildenv(self): ...
    @property
    def runenv(self): ...
    requires: Incomplete
    cpp_info: Incomplete
    _conan_dep_cpp_info: Incomplete
    deps_cpp_info: Incomplete
    env_info: Incomplete
    deps_env_info: Incomplete
    user_info: Incomplete
    deps_user_info: Incomplete
    _conan_env_values: Incomplete
    virtualbuildenv: bool
    virtualrunenv: bool
    def initialize(self, settings, env, buildenv: Incomplete | None = ..., runenv: Incomplete | None = ...) -> None: ...
    @property
    def new_cpp_info(self): ...
    @property
    def source_folder(self): ...
    @property
    def source_path(self) -> Path: ...
    @property
    def export_sources_folder(self): ...
    @property
    def export_sources_path(self) -> Path: ...
    @property
    def export_folder(self): ...
    @property
    def export_path(self) -> Path: ...
    @property
    def build_folder(self): ...
    @property
    def build_path(self) -> Path: ...
    @property
    def package_folder(self): ...
    @property
    def package_path(self) -> Path: ...
    @property
    def install_folder(self): ...
    @property
    def generators_folder(self): ...
    @property
    def generators_path(self) -> Path: ...
    @property
    def imports_folder(self): ...
    @property
    def env(self): ...
    @property
    def channel(self): ...
    @property
    def user(self): ...
    def collect_libs(self, folder: Incomplete | None = ...): ...
    @property
    def build_policy_missing(self): ...
    @property
    def build_policy_always(self): ...
    def source(self) -> None: ...
    def system_requirements(self) -> None: ...
    def config_options(self) -> None: ...
    def configure(self) -> None: ...
    def build(self) -> None: ...
    def package(self) -> None: ...
    def package_info(self) -> None: ...
    def run(self, command, output: bool = ..., cwd: Incomplete | None = ..., win_bash: bool = ..., subsystem: Incomplete | None = ..., msys_mingw: bool = ..., ignore_errors: bool = ..., run_environment: bool = ..., with_login: bool = ..., env: str = ..., scope: str = ...): ...
    def package_id(self) -> None: ...
    def test(self) -> None: ...
    def __repr__(self): ...
