cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project (user_extensions)

set(CMAKE_OSX_ARCHITECTURES "arm64")
set(CMAKE_BUILD_TYPE Debug)

list(APPEND CMAKE_PREFIX_PATH $ENV{ROOTSYS})
find_package(ROOT REQUIRED COMPONENTS Minuit Eve Geom)
include(${ROOT_USE_FILE})
SET(CMAKE_SKIP_BUILD_RPATH FALSE)
SET(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE) 
SET(CMAKE_INSTALL_RPATH "/cvmfs/sft.cern.ch/lcg/releases/vdt/0.4.3-992df/x86_64-centos7-gcc8-opt/lib:/cvmfs/sft.cern.ch/lcg/releases/tbb/2019_U7-ba3eb/x86_64-centos7-gcc8-opt/lib:/cvmfs/sft.cern.ch/lcg/releases/Davix/0.7.3-d94fa/x86_64-centos7-gcc8-opt/lib64/:/cvmfs/sft.cern.ch/lcg/releases/png/1.6.37-9c2fe/x86_64-centos7-gcc8-opt/lib/:/cvmfs/sft.cern.ch/lcg/releases/GSL/2.5-32fc5/x86_64-centos7-gcc8-opt/lib/")
SET(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

find_package(Python3 REQUIRED)
find_package(PythonLibs REQUIRED)

include_directories("${PROJECT_SOURCE_DIR}/include" ${PYTHON_INCLUDE_DIRS})

file(GLOB SOURCES "src/*.cpp")

if(SOURCES)
  add_library(user_extensions ${SOURCES})

  set_property(TARGET user_extensions PROPERTY CXX_STANDARD 17)

  target_link_libraries(user_extensions ${ROOT_LIBRARIES} core extensions histogramming ${PYTHON_LIBRARIES})
  target_include_directories(user_extensions PUBLIC "${PROJECT_SOURCE_DIR}/include")
endif()
