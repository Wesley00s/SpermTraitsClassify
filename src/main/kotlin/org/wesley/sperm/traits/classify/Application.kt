package org.wesley.sperm.traits.classify

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.web.bind.annotation.CrossOrigin
import java.io.File

@CrossOrigin(origins = ["*"])
@SpringBootApplication
class SpermTraitsClassifyApplication

fun main(args: Array<String>) {
    runApplication<SpermTraitsClassifyApplication>(*args)
    val pathFrontend = "/home/wesley/kotlinProjects/SpermTraitsClassify/src/main/react/sperm-bulls-classify-frontend"
    val processReact = ProcessBuilder("npm", "start").directory(File(pathFrontend)).start()
    processReact.waitFor()
}
