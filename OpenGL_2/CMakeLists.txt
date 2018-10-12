cmake_minimum_required(VERSION 3.12)
project(OpenGL_2)

set(CMAKE_CXX_STANDARD 11)
find_package(OpenGL)
find_package(GLUT)

include_directories(${OPENGL_INCLUDE_DIR})
include_directories(${GLUT_INCLUDE_DIR})

add_executable(OpenGL_2 main.cpp)

target_link_libraries(OpenGL_2 ${OPENGL_LIBRARIES} ${GLUT_LIBRARIES})