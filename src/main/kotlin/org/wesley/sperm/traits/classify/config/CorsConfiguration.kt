package org.wesley.sperm.traits.classify.config

import org.springframework.context.annotation.Configuration
import org.springframework.web.servlet.config.annotation.CorsRegistry
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer

@Configuration
class CorsConfiguration : WebMvcConfigurer {
    override fun addCorsMappings(registry: CorsRegistry) {
        registry.addMapping("/**")
            .allowedOriginPatterns("*")
            .allowedMethods("*")
            .allowedMethods("*")
        .allowedHeaders("*")
        .allowCredentials(true)
        .exposedHeaders("*")
        .maxAge(3600)
    }
}