project(chap01)

cmake_minimum_required(VERSION 3.17)

message ("************")
include_directories (
	${PROJECT_SOURCE_DIR}/

)

aux_source_directory(. all_source)

message (${all_source})

add_executable(a.out ${all_source})

