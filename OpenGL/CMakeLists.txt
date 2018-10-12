cmake_minimum_required(VERSION 3.12)
project(OpenGL2)

set(CMAKE_CXX_STANDARD 11)
find_package(OpenGL)
find_package(GLUT)

include_directories(${OPENGL_INCLUDE_DIR})
include_directories(${GLUT_INCLUDE_DIR})

add_executable(OpenGL2 lab2.cpp)

target_link_libraries(OpenGL2 ${OPENGL_LIBRARIES} ${GLUT_LIBRARIES})