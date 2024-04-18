%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-metavision-driver
Version:        1.0.8
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS metavision_driver package

License:        Apache-2
Source0:        %{name}-%{version}.tar.gz

Requires:       OpenSceneGraph
Requires:       OpenSceneGraph-devel
Requires:       OpenThreads
Requires:       OpenThreads-devel
Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       ffmpeg-free-devel
Requires:       glew-devel
Requires:       glfw-devel
Requires:       hdf5-devel
Requires:       libusbx-devel
Requires:       opencv-devel
Requires:       ros-jazzy-event-camera-msgs
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-components
Requires:       ros-jazzy-std-srvs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  OpenSceneGraph
BuildRequires:  OpenSceneGraph-devel
BuildRequires:  OpenThreads
BuildRequires:  OpenThreads-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  cmake3
BuildRequires:  curl
BuildRequires:  ffmpeg-free-devel
BuildRequires:  git
BuildRequires:  glew-devel
BuildRequires:  glfw-devel
BuildRequires:  hdf5
BuildRequires:  hdf5-devel
BuildRequires:  libcurl-devel
BuildRequires:  libusbx-devel
BuildRequires:  opencv-devel
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-ament-cmake-auto
BuildRequires:  ros-jazzy-ament-cmake-ros
BuildRequires:  ros-jazzy-event-camera-msgs
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-components
BuildRequires:  ros-jazzy-ros-environment
BuildRequires:  ros-jazzy-std-srvs
BuildRequires:  unzip
BuildRequires:  wget
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  gtest-devel
BuildRequires:  ros-jazzy-ament-cmake-clang-format
BuildRequires:  ros-jazzy-ament-cmake-copyright
BuildRequires:  ros-jazzy-ament-cmake-cppcheck
BuildRequires:  ros-jazzy-ament-cmake-cpplint
BuildRequires:  ros-jazzy-ament-cmake-flake8
BuildRequires:  ros-jazzy-ament-cmake-lint-cmake
BuildRequires:  ros-jazzy-ament-cmake-pep257
BuildRequires:  ros-jazzy-ament-cmake-xmllint
%endif

%description
ROS1 and ROS2 drivers for metavision based event cameras

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Thu Apr 18 2024 Bernd Pfrommer <bernd.pfrommer@gmail.com> - 1.0.8-3
- Autogenerated by Bloom

* Wed Mar 06 2024 Bernd Pfrommer <bernd.pfrommer@gmail.com> - 1.0.8-2
- Autogenerated by Bloom

