package org.wesley.sperm.traits.classify.controller
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController
import org.wesley.sperm.traits.classify.controller.dto.ReceiveDataDTO
import org.wesley.sperm.traits.classify.service.ReceiveDataService
import java.io.BufferedReader
import java.io.InputStreamReader

@RestController
@RequestMapping("api/data")
class ServiceController(
    private val dataService: ReceiveDataService
) {

    @PostMapping
    fun post(@RequestBody data: ReceiveDataDTO): ResponseEntity<String> {
        dataService.postData(data.to())
        val result = execVerify()
        println(result)
        return ResponseEntity.status(HttpStatus.OK).body(result)
    }

    fun execVerify(): String {
        val command = listOf("/bin/bash", "-c", "source /home/wesley/kotlinProjects/SpermTraitsClassify/src/main/python/SpermTraitsPy/venv/bin/activate && python3 /home/wesley/kotlinProjects/SpermTraitsClassify/src/main/python/SpermTraitsPy/RandomForestModel.py")

        val processBuilder = ProcessBuilder(command)
        processBuilder.redirectErrorStream(true)

        val process = processBuilder.start()

        val reader = BufferedReader(InputStreamReader(process.inputStream))
        val outputBuilder = StringBuilder()
        var line: String? = reader.readLine()
        while (line != null) {
            outputBuilder.append(line).append("\n")
            line = reader.readLine()
        }
        val output = outputBuilder.toString().trim()

        process.waitFor()

        return output
    }
}
