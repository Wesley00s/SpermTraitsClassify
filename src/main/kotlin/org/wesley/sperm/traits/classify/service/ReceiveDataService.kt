package org.wesley.sperm.traits.classify.service

import org.wesley.sperm.traits.classify.model.Data

interface ReceiveDataService {
    fun getData(id: Long): Data
    fun postData(data: Data): Data
}