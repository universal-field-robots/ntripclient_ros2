cmake_minimum_required(VERSION 3.20)
project(ntripclient_ros2)

find_package(ament_cmake REQUIRED)

set(PROJECT_DIRECTORY ${CMAKE_SOURCE_DIR}/ntripclient)
set(COMPILE_DEFINITIONS -Wall -W -O3) # Copied from ntripclient makefile

add_executable(ntripclient ${PROJECT_DIRECTORY}/ntripclient.c ${PROJECT_DIRECTORY}/serial.c)

install(TARGETS ntripclient
    DESTINATION bin
)

install(PROGRAMS scripts/start_ntripclient
    DESTINATION bin
)

install(DIRECTORY launch
    DESTINATION share/${PROJECT_NAME}/
)

ament_package()
