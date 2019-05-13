cmake_minimum_required(VERSION 3.5)

project(ros2_testing NONE)

find_package(ament_cmake_core REQUIRED)
find_package(ament_cmake_export_dependencies REQUIRED)

ament_export_dependencies(
  "launch_testing"
  "launch_testing_ros"
)

ament_package()
