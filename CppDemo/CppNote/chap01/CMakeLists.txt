project(chap01)

cmake_minimum_required(VERSION 3.17)

include_directories (
	${PROJECT_SOURCE_DIR}/

)

aux_source_directory(. all_source)

SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/out)

add_executable(${PROJECT_NAME} ${all_source})

message(STATUS "PROJECT_NAME: ${PROJECT_NAME}")
message(STATUS "PROJECT_SOURCE_DIR: ${PROJECT_SOURCE_DIR}") 
message(STATUS "PROJECT_OUTPUT_DIR: ${EXECUTABLE_OUTPUT_PATH}") 






