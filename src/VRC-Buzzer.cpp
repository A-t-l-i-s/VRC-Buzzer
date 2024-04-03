#include<require.hpp>





int main(int argC, const char* argV[]){
	{
		// Create python config
		PyConfig config;
		PyConfig_InitPythonConfig(&config);

		config.write_bytecode = false;
		config.module_search_paths_set = 0;
		config.pythonpath_env = (wchar_t*)L".;bin;bin.zip;lib;lib.zip;engine.zip;";



		// Initialize python
		Py_InitializeFromConfig(&config);
	}


	{
		// Python script filename
		const char* filename = "VRC-Buzzer.py";

		// Create py string of filename
		PyObject* filenameObj = Py_BuildValue("s", filename);

		// Open file
		FILE* file = _Py_fopen_obj(filenameObj, "rb");

		// Compile file
		PyRun_SimpleFile(file, filename);
	}


	// De-initialize python
	Py_Finalize();


	return 0;
}




