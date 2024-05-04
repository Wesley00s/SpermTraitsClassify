package org.wesley.sperm.traits.classify.service.implement

import org.springframework.stereotype.Service
import org.wesley.sperm.traits.classify.model.Data
import org.wesley.sperm.traits.classify.repositories.ReceiveDataRepository
import org.wesley.sperm.traits.classify.service.ReceiveDataService

@Service
class ReceiveDataServiceImplement (
    private val receiveDataRepository: ReceiveDataRepository
) : ReceiveDataService {
    override fun getData(id: Long): Data {
        return receiveDataRepository.findById(id).orElseThrow()
    }

    override fun postData(data: Data): Data {
        return receiveDataRepository.save(data)
    }
}