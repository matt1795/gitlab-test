cmake_minimum_required(VERSION 3.10)
project(test)

add_library(${PROJECT_NAME} src/test.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC include)
